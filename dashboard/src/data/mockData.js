export function generateLatencyData(points = 20) {
  const data = []
  const now = new Date()
  for (let i = points; i > 0; i--) {
    const time = new Date(now.getTime() - i * 60000)
    data.push({
      time: time.toLocaleTimeString('en-US', { hour12: false, hour: '2-digit', minute: '2-digit' }),
      latency: Math.floor(Math.random() * 150 + 50),
      p95: Math.floor(Math.random() * 300 + 150),
    })
  }
  return data
}

export function generateThroughputData(points = 12) {
  const data = []
  const now = new Date()
  for (let i = points; i > 0; i--) {
    const time = new Date(now.getTime() - i * 3600000)
    data.push({
      time: time.toLocaleTimeString('en-US', { hour12: false, hour: '2-digit' }) + ':00',
      requests: Math.floor(Math.random() * 500 + 200),
    })
  }
  return data
}

export function generateEvents(count = 10) {
  const services = ['api-gateway', 'payment-service', 'user-worker', 'notification-svc']
  const actions = ['POST /api/v1/orders', 'GET /api/v1/users/{id}', 'AuthorizePayment', 'SendPushNotification']
  const apps = ['web-app', 'mobile-ios', 'mobile-android', 'admin-panel']

  return Array.from({ length: count }).map((_, i) => {
    const now = new Date(Date.now() - i * 45000)
    return {
      id: `evt-${1000 + i}`,
      timestamp: now.toISOString(),
      app: apps[Math.floor(Math.random() * apps.length)],
      service: services[Math.floor(Math.random() * services.length)],
      action: actions[Math.floor(Math.random() * actions.length)],
      context: {
        latency_ms: Math.floor(Math.random() * 300 + 40),
        request_id: `req-${Math.random().toString(36).substr(2, 9)}`,
        provider: Math.random() > 0.8 ? 'Stripe' : null,
      },
    }
  })
}

export function getInitialMetrics() {
  return {
    errorRate: (Math.random() * 0.5 + 0.1).toFixed(2),
    latency: Math.floor(Math.random() * 120 + 80),
    throughput: Math.floor(Math.random() * 1200 + 800),
    dbPool: Math.floor(Math.random() * 40 + 10),
  }
}
