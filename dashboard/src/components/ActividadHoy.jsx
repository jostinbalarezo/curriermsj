import { Clock } from 'lucide-react'

export default function ActividadHoy({ data, total }) {
  const maxVal = Math.max(...data.map(d => d.envios), 1)

  return (
    <div className="glass-card p-5 md:p-6 h-full">
      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-success/10 flex items-center justify-center">
            <Clock className="w-5 h-5 text-success" />
          </div>
          <div>
            <h3 className="text-base font-semibold text-text-primary">Actividad Hoy</h3>
            <p className="text-text-muted text-xs">{total} envíos registrados</p>
          </div>
        </div>
      </div>

      {/* Vertical bar visualization */}
      <div className="space-y-1.5">
        {data.map((item) => (
          <div key={item.hora} className="flex items-center gap-3 group">
            <span className="text-text-muted text-[11px] font-mono w-10 shrink-0 tabular-nums">
              {item.hora}
            </span>
            <div className="flex-1 h-5 bg-surface-hover/50 rounded-md overflow-hidden relative">
              <div
                className="h-full bg-gradient-to-r from-success/60 to-success rounded-md transition-all duration-700 ease-out"
                style={{ width: item.envios > 0 ? `${Math.max((item.envios / maxVal) * 100, 6)}%` : '0%' }}
              />
              {item.envios > 0 && (
                <span className="absolute right-2 top-1/2 -translate-y-1/2 text-[10px] font-bold text-text-primary">
                  {item.envios}
                </span>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
