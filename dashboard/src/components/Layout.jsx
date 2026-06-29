import React from 'react'
import Sidebar from './Sidebar'

export default function Layout({ children, currentView, setView, error }) {
  return (
    <div className="flex h-screen w-screen overflow-hidden bg-surface text-text-primary">
      {/* Left Sidebar */}
      <Sidebar currentView={currentView} setView={setView} error={error} />

      {/* Main Content Area */}
      <div className="flex-1 flex flex-col min-w-0 overflow-hidden">
        {/* Header */}
        <header className="h-16 bg-surface-alt/80 backdrop-blur-xl border-b border-border flex items-center justify-between px-6 shrink-0">
          <div className="flex items-center gap-3">
            <span className="font-bold text-sm text-text-secondary">CurrierMsj Console</span>
            <span className="text-text-muted">/</span>
            <span className="text-xs text-text-muted bg-surface-card px-2.5 py-1 rounded-full border border-border">
              {currentView === 'courier' ? 'Gestión de Envíos' : 'Observabilidad de Sistemas'}
            </span>
          </div>
          <div className="flex items-center gap-3">
            <span className="text-xs font-mono text-text-muted bg-surface-card px-2.5 py-1 rounded border border-border">
              127.0.0.1:5173
            </span>
          </div>
        </header>

        {/* Content Body */}
        <main className="flex-1 overflow-y-auto bg-surface">
          {children}
        </main>
      </div>
    </div>
  )
}
