// Microservicio 1: Node.js + Firebase (Cloud Firestore)
// Autora: Antonela - rama feat/firebase-node
const path = require('path');
const express = require('express');
const admin = require('firebase-admin');

// La clave privada NO se sube al repo (ver .gitignore).
const keyPath =
  process.env.GOOGLE_APPLICATION_CREDENTIALS ||
  path.join(__dirname, 'serviceAccountKey.json');

admin.initializeApp({
  credential: admin.credential.cert(require(keyPath)),
});

const db = admin.firestore();
const COLECCION = 'reproducciones';

const app = express();
app.use(express.json());

// Estado del servicio
app.get('/health', (req, res) => res.json({ status: 'ok' }));

// Registrar una reproduccion (telemetria)
app.post('/reproducciones', async (req, res) => {
  try {
    const { usuario, trackId, titulo } = req.body;
    if (!usuario || !trackId) {
      return res.status(400).json({ error: 'usuario y trackId son obligatorios' });
    }
    const ref = await db.collection(COLECCION).add({
      usuario,
      trackId,
      titulo: titulo || null,
      fecha: admin.firestore.FieldValue.serverTimestamp(),
    });
    res.status(201).json({ id: ref.id });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Error al guardar en Firestore' });
  }
});

// Consultar las ultimas reproducciones
app.get('/reproducciones', async (req, res) => {
  try {
    const snap = await db
      .collection(COLECCION)
      .orderBy('fecha', 'desc')
      .limit(20)
      .get();
    res.json(snap.docs.map((d) => ({ id: d.id, ...d.data() })));
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Error al consultar Firestore' });
  }
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, async () => {
  console.log(`Microservicio Node escuchando en http://localhost:${PORT}`);
  // Registro inicial: evidencia de persistencia al arrancar
  try {
    const ref = await db.collection(COLECCION).add({
      usuario: 'demo',
      trackId: 0,
      titulo: 'Registro inicial de arranque',
      fecha: admin.firestore.FieldValue.serverTimestamp(),
    });
    console.log('Registro inicial guardado en Firestore, id:', ref.id);
  } catch (err) {
    console.error('No se pudo guardar el registro inicial:', err.message);
  }
});