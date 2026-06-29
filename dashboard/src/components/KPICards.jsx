import { Package, CalendarDays, TrendingUp, Users, MapPin, Layers } from 'lucide-react'

function AnimatedNumber({ value, loading }) {
  if (loading) {
    return <div className="h-8 w-20 bg-surface-hover rounded-lg animate-pulse" />
  }
  return (
    <span className="text-2xl md:text-3xl font-extrabold text-text-primary tabular-nums animate-count-up">
      {typeof value === 'number' ? value.toLocaleString('es-EC') : value}
    </span>
  )
}

export default function KPICards({ metricas, loading }) {
  const cards = [
    {
      label: 'Total Envíos',
      value: metricas.totalEnvios,
      icon: Package,
      gradient: 'from-brand-500/20 to-brand-700/5',
      iconColor: 'text-brand-400',
      borderGlow: 'hover:shadow-brand-500/10',
    },
    {
      label: 'Hoy',
      value: metricas.enviosHoy,
      icon: CalendarDays,
      gradient: 'from-success/20 to-success/5',
      iconColor: 'text-success',
      borderGlow: 'hover:shadow-success/10',
    },
    {
      label: 'Esta Semana',
      value: metricas.enviosSemana,
      icon: TrendingUp,
      gradient: 'from-info/20 to-info/5',
      iconColor: 'text-info',
      borderGlow: 'hover:shadow-info/10',
    },
    {
      label: 'Este Mes',
      value: metricas.enviosMes,
      icon: Layers,
      gradient: 'from-warning/20 to-warning/5',
      iconColor: 'text-warning',
      borderGlow: 'hover:shadow-warning/10',
    },
    {
      label: 'Clientes',
      value: metricas.clientesUnicos,
      icon: Users,
      gradient: 'from-danger/20 to-danger/5',
      iconColor: 'text-danger',
      borderGlow: 'hover:shadow-danger/10',
    },
    {
      label: 'Destinos',
      value: metricas.destinosUnicos,
      icon: MapPin,
      gradient: 'from-brand-400/20 to-brand-600/5',
      iconColor: 'text-brand-300',
      borderGlow: 'hover:shadow-brand-400/10',
    },
  ]

  return (
    <div id="kpi-cards" className="grid grid-cols-2 md:grid-cols-3 xl:grid-cols-6 gap-3 md:gap-4">
      {cards.map((card, idx) => (
        <div
          key={card.label}
          id={`kpi-${card.label.toLowerCase().replace(/\s/g, '-')}`}
          className={`glass-card p-4 md:p-5 bg-gradient-to-br ${card.gradient} animate-fade-in stagger-${idx + 1} group cursor-default ${card.borderGlow} hover:shadow-xl transition-all duration-300`}
        >
          <div className="flex items-center justify-between mb-3">
            <span className="text-text-secondary text-xs font-semibold uppercase tracking-wider">{card.label}</span>
            <card.icon className={`w-5 h-5 ${card.iconColor} opacity-70 group-hover:opacity-100 group-hover:scale-110 transition-all duration-300`} />
          </div>
          <AnimatedNumber value={card.value} loading={loading} />
        </div>
      ))}
    </div>
  )
}
