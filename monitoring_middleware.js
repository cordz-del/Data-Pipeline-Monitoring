// monitoring_middleware.js
const morgan = require('morgan');
const client = require('prom-client');

// Collect default system metrics
client.collectDefaultMetrics();

// Create a counter metric for HTTP requests
const httpRequestCounter = new client.Counter({
  name: 'http_request_total',
  help: 'Total number of HTTP requests',
  labelNames: ['method', 'route', 'status']
});

// Custom middleware to count requests
function prometheusMiddleware(req, res, next) {
  res.on('finish', () => {
    httpRequestCounter.inc({
      method: req.method,
      route: req.originalUrl,
      status: res.statusCode
    });
  });
  next();
}

module.exports = { morgan, prometheusMiddleware, client };
