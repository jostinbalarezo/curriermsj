import React from 'react'

export default function StatusConexion({ error }) {
  if (error) {
    return (
      <div 
        id="status-connection-error" 
        className="flex items-center gap-2 px-3 py-1.5 rounded-full bg-danger/10 text-danger border border-danger/20 text-xs font-semibold"
        title={error}
      >
        <span className="w-2 h-2 rounded-full bg-danger animate-pulse" />
        <span>Error de Conexión</span>
      </div>
    )
  }

  return (
    <div 
      id="status-connection-ok" 
      className="flex items-center gap-2 px-3 py-1.5 rounded-full bg-success/10 text-success border border-success/20 text-xs font-semibold"
    >
      <span className="w-2 h-2 rounded-full bg-success animate-pulse-glow" />
      <span>Conectado a Supabase</span>
    </div>
  )
}
