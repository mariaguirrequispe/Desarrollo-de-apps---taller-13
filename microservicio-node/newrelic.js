'use strict'
/**
 * Configuracion del agente APM de New Relic.
 * La License Key NO se escribe aqui: se toma de la variable de entorno
 * NEW_RELIC_LICENSE_KEY (region United States) para no exponerla en el repositorio.
 *   export NEW_RELIC_LICENSE_KEY=xxxxxxxxxxxxxxxxxxxxNRAL
 */
exports.config = {
  app_name: ['microservicio-telemetria-node'],
  license_key: process.env.NEW_RELIC_LICENSE_KEY || 'PEGAR_AQUI_LICENSE_KEY',
  distributed_tracing: { enabled: true },
  logging: { level: 'info' },
  allow_all_headers: true,
  application_logging: { forwarding: { enabled: true } },
  attributes: {
    exclude: [
      'request.headers.cookie',
      'request.headers.authorization',
      'request.headers.proxyAuthorization',
      'request.headers.setCookie*',
      'request.headers.x*',
      'response.headers.cookie',
      'response.headers.authorization',
      'response.headers.proxyAuthorization',
      'response.headers.setCookie*',
      'response.headers.x*'
    ]
  }
}
