import { useEffect, useState } from 'react'
import { AlertCircle, CheckCircle2, Server, ShieldAlert, WifiOff } from 'lucide-react'
import { hasSupabaseConfig, supabase } from '../lib/supabaseClient'

const botHealthUrl = import.meta.env.VITE_BOT_HEALTH_URL || 'http://localhost:5000/health'

export default function ServiceStatus() {
  const [services, setServices] = useState([
    { name: 'Bot Flask', state: 'checking', message: 'Verificando backend local...' },
    { name: 'Supabase', state: 'checking', message: 'Verificando configuracion...' },
    { name: 'WhatsApp API', state: 'warning', message: 'No se prueba desde frontend por seguridad.' },
  ])

  useEffect(() => {
    async function checkServices() {
      await Promise.all([checkBot(), checkSupabase()])
    }
    checkServices()
  }, [])

  async function checkBot() {
    try {
      const response = await fetch(botHealthUrl, { cache: 'no-store' })
      if (!response.ok) throw new Error(`HTTP ${response.status}`)
      const data = await response.json()
      updateService('Bot Flask', 'ok', data.service ? `Activo: ${data.service}` : 'Backend activo')
    } catch {
      updateService(
        'Bot Flask',
        'down',
        'No abre el backend. Ejecuta: cd bot-mensajeria && python app.py'
      )
    }
  }

  async function checkSupabase() {
    if (!hasSupabaseConfig || !supabase) {
      updateService('Supabase', 'warning', 'Sin VITE_SUPABASE_URL / VITE_SUPABASE_ANON_KEY')
      return
    }

    try {
      const { error } = await supabase.auth.getSession()
      if (error) throw error
      updateService('Supabase', 'ok', 'Cliente configurado')
    } catch {
      updateService('Supabase', 'down', 'No conecta con la configuracion actual')
    }
  }

  function updateService(name, state, message) {
    setServices((current) =>
      current.map((service) => (service.name === name ? { ...service, state, message } : service))
    )
  }

  return (
    <section className="bg-slate-900 rounded-xl p-5 border border-slate-800 shadow-sm">
      <div className="flex items-center gap-2 mb-4">
        <AlertCircle className="w-5 h-5 text-sky-400" />
        <h3 className="text-lg font-semibold text-slate-200">Estado de servicios</h3>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
        {services.map((service) => (
          <article key={service.name} className="p-4 bg-slate-800/50 rounded-lg border border-slate-700/60">
            <div className="flex items-start justify-between gap-3">
              <div className="flex items-center gap-3">
                <StatusIcon state={service.state} />
                <div>
                  <div className="font-medium text-slate-100">{service.name}</div>
                  <div className="text-xs text-slate-400 mt-1">{service.message}</div>
                </div>
              </div>
              <StatusBadge state={service.state} />
            </div>
          </article>
        ))}
      </div>

      <p className="mt-4 text-xs text-slate-500">
        WhatsApp Cloud API no debe probarse desde React porque expondria el token. Si falla, el backend debe
        mostrarlo en logs o en un endpoint seguro.
      </p>
    </section>
  )
}

function StatusIcon({ state }) {
  if (state === 'checking') {
    return <Server className="w-5 h-5 text-sky-400 animate-pulse" />
  }
  if (state === 'ok') {
    return <CheckCircle2 className="w-5 h-5 text-emerald-400" />
  }
  if (state === 'warning') {
    return <ShieldAlert className="w-5 h-5 text-amber-400" />
  }
  return <WifiOff className="w-5 h-5 text-rose-400" />
}

function StatusBadge({ state }) {
  const styles = {
    checking: 'bg-sky-500/10 text-sky-300',
    ok: 'bg-emerald-500/10 text-emerald-300',
    warning: 'bg-amber-500/10 text-amber-300',
    down: 'bg-rose-500/10 text-rose-300',
  }
  const labels = {
    checking: 'Revisando',
    ok: 'OK',
    warning: 'Atencion',
    down: 'Falla',
  }

  return (
    <span className={`text-xs font-semibold px-2 py-1 rounded-full ${styles[state] || styles.down}`}>
      {labels[state] || 'Falla'}
    </span>
  )
}
