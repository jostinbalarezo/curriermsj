import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Cell } from 'recharts'
import { TrendingUp } from 'lucide-react'

const CustomTooltip = ({ active, payload, label }) => {
  if (!active || !payload?.length) return null
  return (
    <div className="bg-surface-card border border-border rounded-xl px-4 py-3 shadow-2xl">
      <p className="text-text-secondary text-xs font-medium mb-1">{label}</p>
      <p className="text-text-primary text-lg font-bold">{payload[0].value} envíos</p>
    </div>
  )
}

export default function EnviosChart({ data }) {
  const maxVal = Math.max(...data.map(d => d.envios), 1)

  return (
    <div className="glass-card p-5 md:p-6 h-full">
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-brand-500/10 flex items-center justify-center">
            <TrendingUp className="w-5 h-5 text-brand-400" />
          </div>
          <div>
            <h3 className="text-base font-semibold text-text-primary">Envíos por Día</h3>
            <p className="text-text-muted text-xs">Últimos 7 días</p>
          </div>
        </div>
      </div>
      <div className="h-64">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data} barCategoryGap="20%">
            <CartesianGrid strokeDasharray="3 3" stroke="oklch(0.25 0.02 270)" vertical={false} />
            <XAxis
              dataKey="dia"
              stroke="oklch(0.50 0.02 270)"
              tick={{ fontSize: 12, fill: 'oklch(0.50 0.02 270)' }}
              axisLine={false}
              tickLine={false}
            />
            <YAxis
              stroke="oklch(0.50 0.02 270)"
              tick={{ fontSize: 12, fill: 'oklch(0.50 0.02 270)' }}
              axisLine={false}
              tickLine={false}
              allowDecimals={false}
            />
            <Tooltip content={<CustomTooltip />} cursor={{ fill: 'oklch(0.22 0.025 270 / 0.5)' }} />
            <Bar dataKey="envios" radius={[8, 8, 4, 4]} maxBarSize={48}>
              {data.map((entry, index) => (
                <Cell
                  key={`cell-${index}`}
                  fill={entry.envios === maxVal ? 'oklch(0.58 0.20 270)' : 'oklch(0.58 0.20 270 / 0.4)'}
                />
              ))}
            </Bar>
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  )
}
