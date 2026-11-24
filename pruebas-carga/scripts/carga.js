// Prueba de carga concurrente sin dependencias (Node >= 18).
// Uso: node carga.js <url> [total=300] [concurrencia=100] [metodo=GET] [cuerpoJSON]
const [url, total = 300, conc = 100, metodo = 'GET', cuerpo] = process.argv.slice(2);
if (!url) { console.log('Uso: node carga.js <url> [total] [concurrencia] [metodo] [cuerpoJSON]'); process.exit(1); }
const N = +total, C = +conc; const tiempos = []; let ok = 0, err = 0, i = 0;
async function worker() {
  while (i < N) {
    i++; const t0 = performance.now();
    try {
      const r = await fetch(url, { method: metodo, headers: { 'Content-Type': 'application/json' }, body: cuerpo });
      await r.text(); (r.status < 400 ? ok++ : err++);
    } catch { err++; }
    tiempos.push(performance.now() - t0);
  }
}
const t0 = performance.now();
Promise.all(Array.from({ length: C }, worker)).then(() => {
  const seg = (performance.now() - t0) / 1000; tiempos.sort((a, b) => a - b);
  const p = q => tiempos[Math.min(tiempos.length - 1, Math.floor(q * tiempos.length))].toFixed(1);
  console.log(JSON.stringify({ url, metodo, total: N, concurrencia: C, exitosas: ok, errores: err,
    duracion_s: +seg.toFixed(2), throughput_rps: +(N / seg).toFixed(1),
    ms: { min: tiempos[0].toFixed(1), p50: p(.5), p95: p(.95), p99: p(.99), max: tiempos.at(-1).toFixed(1) } }, null, 2));
});
