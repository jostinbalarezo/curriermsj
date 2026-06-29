import React from 'react'
import { Package, Activity, Terminal, ShieldAlert, Cpu } from 'lucide-react'
import StatusConexion from './StatusConexion'

export default function Sidebar({ currentView, setView, error }) {
  const navigation = [
    { id: 'courier', name: 'Gestión Courier', icon: Package, description: 'Envíos, clientes y rutas' },
    { id: 'system', name: 'Observabilidad Técnica', icon: Activity, description: 'Salud, latencia y logs' },
  ]

  return (
    <aside className="w-80 bg-surface-alt border-r border-border flex flex-col shrink-0">
      {/* Brand Header */}
      <div className="h-16 flex items-center px-6 border-b border-border gap-3">
        <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-brand-500 to-brand-700 flex items-center justify-center shadow-lg shadow-brand-600/20">
          <Terminal className="w-4.5 h-4.5 text-white" />
        </div>
        <div>
          <span className="font-bold text-base text-text-primary tracking-tight">CurrierMsj</span>
          <span className="text-[10px] text-text-muted block font-medium uppercase tracking-wider">Console v1.2</span>
        </div>
      </div>

      {/* Navigation */}
      <nav className="flex-1 p-4 space-y-2">
        {navigation.map((item) => {
          const isActive = currentView === item.id
          return (
            <button
              key={item.id}
              onClick={() => setView(item.id)}
              className={`w-full text-left flex items-start gap-3.5 px-4 py-3 rounded-xl transition-all duration-200 group ${
                isActive
                  ? 'bg-brand-500/10 text-brand-400 border border-brand-500/20 shadow-sm shadow-brand-500/5'
                  : 'text-text-secondary hover:bg-surface-hover hover:text-text-primary border border-transparent'
              }`}
            >
              <item.icon className={`w-5 h-5 shrink-0 mt-0.5 transition-transform duration-200 ${isActive ? 'text-brand-400' : 'text-text-muted group-hover:text-text-primary group-hover:scale-105'}`} />
              <div className="min-w-0">
                <div className="text-sm font-semibold tracking-tight">{item.name}</div>
                <div className="text-[11px] text-text-muted mt-0.5 truncate">{item.description}</div>
              </div>
            </button>
          )
        })}
      </nav>

      {/* Footer / Status Area */}
      <div className="p-4 border-t border-border bg-surface/50 space-y-3">
        <div className="flex items-center justify-between text-xs text-text-secondary">
          <span className="font-medium">Servidor</span>
          <span className="font-mono text-text-muted bg-surface-card px-2 py-0.5 rounded border border-border">production</span>
        </div>
        <StatusConexion error={error} />
      </div>
    </aside>
  )
}
