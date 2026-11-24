# 100 peticiones concurrentes (Node >= 18). Los servicios deben estar corriendo.
$s = "$PSScriptRoot\scripts\carga.js"
$out = "$PSScriptRoot\evidencias"
node $s http://localhost:3000/health 500 100 | Tee-Object "$out\carga_node_health_GET.json"
node $s http://localhost:3000/reproducciones 300 100 | Tee-Object "$out\carga_node_reproducciones_GET.json"
node $s http://localhost:3000/reproducciones 200 100 POST '{"usuario":"carga","trackId":1,"titulo":"prueba"}' | Tee-Object "$out\carga_node_reproducciones_POST.json"
node $s http://localhost:8000/api/albumes/ 500 100 | Tee-Object "$out\carga_django_albumes_GET.json"
