import { useState } from 'react'
import { useEnvios, useSystemStats, calcularMetricas } from './lib/useSupabase'
import Layout from './components/Layout'
import KPICards from './components/KPICards'
import EnviosChart from './components/EnviosChart'
import TiposPaqueteChart from './components/TiposPaqueteChart'
import EnviosTable from './components/EnviosTable'
import ActividadHoy from './components/ActividadHoy'
import SystemObservability from './components/SystemObservability'

function App() {
  const [view, setView] = useState('courier') // 'courier' o 'system'
  const { envios, loading: loadingEnvios, error: errorEnvios, refetch: refetchEnvios } = useEnvios()
  const { stats, loading: loadingStats, error: errorStats, refetch: refetchStats } = useSystemStats()
  const metricas = calcularMetricas(envios)

  // Usamos el error de envíos como proxy del estado de la conexión general
  const connectionError = errorEnvios || errorStats

  return (
    <Layout currentView={view} setView={setView} error={connectionError}>
      {view === 'courier' ? (
        <div className="p-4 md:p-8 space-y-6 max-w-[1600px] mx-auto">
          {/* Header */}
          <header className="flex flex-col md:flex-row md:items-center justify-between gap-4 animate-fade-in">
            <div>
              <h1 className="text-2xl md:text-3xl font-bold text-text-primary tracking-tight">
                Gestión Courier
              </h1>
              <p className="text-text-secondary text-sm mt-1">
                Monitoreo y administración de envíos de usuarios de CurrierMsj
              </p>
            </div>
            <div className="flex items-center gap-3">
              <button
                id="btn-refetch"
                onClick={refetchEnvios}
                className="px-4 py-2 text-sm font-medium rounded-xl bg-brand-600 text-white hover:bg-brand-500 active:scale-95 transition-all duration-200 shadow-lg shadow-brand-600/20"
              >
                ↻ Actualizar Envíos
              </button>
            </div>
          </header>

          {/* KPI Cards */}
          <KPICards metricas={metricas} loading={loadingEnvios} />

          {/* Charts Row */}
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className="lg:col-span-2 animate-fade-in stagger-3">
              <EnviosChart data={metricas.enviosPorDia} />
            </div>
            <div className="animate-fade-in stagger-4">
              <TiposPaqueteChart data={metricas.tiposOrdenados} total={metricas.totalEnvios} />
            </div>
          </div>

          {/* Activity + Table */}
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className="animate-fade-in stagger-4">
              <ActividadHoy data={metricas.enviosPorHora} total={metricas.enviosHoy} />
            </div>
            <div className="lg:col-span-2 animate-fade-in stagger-5">
              <EnviosTable envios={envios} loading={loadingEnvios} />
            </div>
          </div>
        </div>
      ) : (
        <SystemObservability 
          systemStats={stats} 
          loadingStats={loadingStats} 
          refetchStats={refetchStats} 
        />
      )}
    </Layout>
  )
}

export default App
