import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip } from 'recharts'
import { Layers } from 'lucide-react'

const COLORS = [
  'oklch(0.58 0.20 270)',
  'oklch(0.72 0.19 160)',
  'oklch(0.80 0.16 85)',
  'oklch(0.72 0.15 230)',
  'oklch(0.65 0.22 25)',
  'oklch(0.68 0.16 270)',
]

const CustomTooltip = ({ active, payload }) => {
  if (!active || !payload?.length) return null
  const item = payload[0]
  return (
    <div className="bg-surface-card border border-border rounded-xl px-4 py-3 shadow-2xl">
      <p className="text-text-primary text-sm font-semibold">{item.name}</p>
      <p className="text-text-secondary text-xs mt-1">{item.value} envíos</p>
    </div>
  )
}

export default function TiposPaqueteChart({ data, total }) {
  const chartData = data.map(item => ({
    name: item.nombre.replace(/\s*[\u{1F4C4}\u{1F4E6}\u{2709}]\s*/gu, '').trim(),
    value: item.cantidad,
  }))

  if (chartData.length === 0) {
    return (
      <div className="glass-card p-5 md:p-6 h-full flex flex-col items-center justify-center text-text-muted">
        <Layers className="w-10 h-10 mb-3 opacity-40" />
        <p className="text-sm">Sin datos de tipos de paquete</p>
      </div>
    )
  }

  return (
    <div className="glass-card p-5 md:p-6 h-full">
      <div className="flex items-center gap-3 mb-6">
        <div className="w-10 h-10 rounded-xl bg-warning/10 flex items-center justify-center">
          <Layers className="w-5 h-5 text-warning" />
        </div>
        <div>
          <h3 className="text-base font-semibold text-text-primary">Tipos de Paquete</h3>
          <p className="text-text-muted text-xs">{total} envíos totales</p>
        </div>
      </div>

      <div className="h-44 mb-4">
        <ResponsiveContainer width="100%" height="100%">
          <PieChart>
            <Pie
              data={chartData}
              cx="50%"
              cy="50%"
              innerRadius={50}
              outerRadius={75}
              paddingAngle={3}
              dataKey="value"
              strokeWidth={0}
            >
              {chartData.map((_, index) => (
                <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
              ))}
            </Pie>
            <Tooltip content={<CustomTooltip />} />
          </PieChart>
        </ResponsiveContainer>
      </div>

      {/* Legend */}
      <div className="space-y-2">
        {chartData.slice(0, 5).map((item, idx) => (
          <div key={item.name} className="flex items-center justify-between text-sm">
            <div className="flex items-center gap-2">
              <div
                className="w-2.5 h-2.5 rounded-full shrink-0"
                style={{ backgroundColor: COLORS[idx % COLORS.length] }}
              />
              <span className="text-text-secondary text-xs truncate max-w-[140px]">{item.name}</span>
            </div>
            <span className="text-text-primary font-semibold text-xs tabular-nums">{item.value}</span>
          </div>
        ))}
      </div>
    </div>
  )
}
