// Microservicio de telemetria: Node.js + Express + Firebase Admin (Cloud Firestore)
const express = require('express');
const admin = require('firebase-admin');
const path = require('path');

// La clave privada se lee de un archivo FUERA del control de versiones (.gitignore)
// o de la variable GOOGLE_APPLICATION_CREDENTIALS_PATH.
const keyPath = process.env.GOOGLE_APPLICATION_CREDENTIALS_PATH
  || path.join(__dirname, 'serviceAccountKey.json');
const serviceAccount = require(keyPath);

admin.initializeApp({ credential: admin.credential.cert(serviceAccount) });
const db = admin.firestore();
const COLECCION = 'reproducciones';

const app = express();
app.use(express.json());

app.get('/health', (req, res) => {
  res.json({ status: 'ok', servicio: 'telemetria', timestamp: new Date().toISOString() });
});

app.post('/reproducciones', async (req, res) => {
  const { usuario, trackId, titulo } = req.body || {};
  if (!usuario || trackId === undefined || !titulo) {
    return res.status(400).json({ error: 'usuario, trackId y titulo son obligatorios' });
  }
  try {
    const ref = await db.collection(COLECCION).add({
      usuario, trackId, titulo,
      fecha: admin.firestore.FieldValue.serverTimestamp(),
    });
    res.status(201).json({ id: ref.id });
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.get('/reproducciones', async (req, res) => {
  try {
    const snap = await db.collection(COLECCION).orderBy('fecha', 'desc').limit(20).get();
    res.json(snap.docs.map(d => ({ id: d.id, ...d.data() })));
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, async () => {
  console.log(`Microservicio de telemetria escuchando en el puerto ${PORT}`);
  // Registro inicial al arrancar (requisito: persistir al menos un registro)
  try {
    const ref = await db.collection(COLECCION).add({
      usuario: 'sistema', trackId: 0, titulo: 'Registro inicial de arranque',
      fecha: admin.firestore.FieldValue.serverTimestamp(),
    });
    console.log('Registro inicial guardado en Firestore con id:', ref.id);
  } catch (e) {
    console.error('No se pudo guardar el registro inicial:', e.message);
  }
});
