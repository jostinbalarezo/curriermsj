import { useState } from 'react'
import { Package, User, Phone, MapPin, Calendar, Clock as ClockIcon, FileText, ChevronDown, ChevronUp, Search } from 'lucide-react'

function formatFecha(fechaStr) {
  if (!fechaStr) return '—'
  try {
    const date = new Date(fechaStr)
    return date.toLocaleDateString('es-EC', {
      day: '2-digit',
      month: 'short',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    })
  } catch {
    return fechaStr
  }
}

function EnvioRow({ envio, isExpanded, onToggle }) {
  return (
    <>
      <tr
        onClick={onToggle}
        className="border-b border-border/50 hover:bg-surface-hover/40 transition-colors cursor-pointer group"
      >
        <td className="px-4 py-3.5">
          <span className="text-text-primary font-semibold text-sm">#{envio.id}</span>
        </td>
        <td className="px-4 py-3.5">
          <div className="flex items-center gap-2">
            <div className="w-7 h-7 rounded-full bg-brand-500/10 flex items-center justify-center shrink-0">
              <User className="w-3.5 h-3.5 text-brand-400" />
            </div>
            <div className="min-w-0">
              <div className="text-text-primary text-sm font-medium truncate max-w-[140px]">
                {envio.remitente || '—'}
              </div>
              <div className="text-text-muted text-[11px] truncate max-w-[140px]">
                {envio.telefono_remitente || ''}
              </div>
            </div>
          </div>
        </td>
        <td className="px-4 py-3.5">
          <div className="min-w-0">
            <div className="text-text-primary text-sm font-medium truncate max-w-[140px]">
              {envio.destinatario || '—'}
            </div>
            <div className="text-text-muted text-[11px] truncate max-w-[140px]">
              {envio.telefono_destinatario || ''}
            </div>
          </div>
        </td>
        <td className="px-4 py-3.5 hidden lg:table-cell">
          <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium bg-brand-500/10 text-brand-300 border border-brand-500/20">
            <Package className="w-3 h-3" />
            {(envio.tipo_paquete || '—').replace(/\s*[\u{1F4C4}\u{1F4E6}\u{2709}]\s*/gu, '').trim()}
          </span>
        </td>
        <td className="px-4 py-3.5 hidden md:table-cell">
          <span className="text-text-secondary text-xs font-mono">{formatFecha(envio.creado_en)}</span>
        </td>
        <td className="px-4 py-3.5 text-right">
          {isExpanded ? (
            <ChevronUp className="w-4 h-4 text-text-muted inline" />
          ) : (
            <ChevronDown className="w-4 h-4 text-text-muted inline group-hover:text-brand-400 transition-colors" />
          )}
        </td>
      </tr>
      {isExpanded && (
        <tr className="bg-surface-hover/20 border-b border-border/30">
          <td colSpan={6} className="px-6 py-4">
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 text-sm animate-fade-in">
              <InfoItem icon={MapPin} label="Origen" value={envio.direccion_origen} />
              <InfoItem icon={MapPin} label="Destino" value={envio.direccion_destino} />
              <InfoItem icon={Package} label="Peso" value={envio.peso} />
              <InfoItem icon={Package} label="Dimensiones" value={envio.dimensiones} />
              <InfoItem icon={Calendar} label="Fecha envío" value={envio.fecha_envio} />
              <InfoItem icon={ClockIcon} label="Hora envío" value={envio.hora_envio} />
              <InfoItem icon={FileText} label="Instrucciones" value={envio.instrucciones} className="md:col-span-2 lg:col-span-3" />
            </div>
          </td>
        </tr>
      )}
    </>
  )
}

function InfoItem({ icon: Icon, label, value, className = '' }) {
  return (
    <div className={`flex items-start gap-2 ${className}`}>
      <Icon className="w-4 h-4 text-text-muted mt-0.5 shrink-0" />
      <div>
        <div className="text-text-muted text-[11px] uppercase tracking-wider font-semibold">{label}</div>
        <div className="text-text-primary text-sm mt-0.5">{value || '—'}</div>
      </div>
    </div>
  )
}

export default function EnviosTable({ envios, loading }) {
  const [expandedId, setExpandedId] = useState(null)
  const [busqueda, setBusqueda] = useState('')

  const filtrados = envios.filter(e => {
    if (!busqueda) return true
    const q = busqueda.toLowerCase()
    return (
      (e.remitente || '').toLowerCase().includes(q) ||
      (e.destinatario || '').toLowerCase().includes(q) ||
      (e.telefono_remitente || '').includes(q) ||
      (e.telefono_destinatario || '').includes(q) ||
      (e.direccion_destino || '').toLowerCase().includes(q) ||
      String(e.id).includes(q)
    )
  })

  if (loading) {
    return (
      <div className="glass-card p-6 h-full">
        <div className="flex items-center gap-3 mb-6">
          <div className="w-10 h-10 rounded-xl bg-info/10 flex items-center justify-center">
            <Package className="w-5 h-5 text-info" />
          </div>
          <h3 className="text-base font-semibold text-text-primary">Envíos Recientes</h3>
        </div>
        <div className="space-y-3">
          {[...Array(5)].map((_, i) => (
            <div key={i} className="h-14 bg-surface-hover/50 rounded-lg animate-pulse" />
          ))}
        </div>
      </div>
    )
  }

  return (
    <div className="glass-card overflow-hidden h-full flex flex-col">
      <div className="p-5 md:p-6 pb-0">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-5">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-info/10 flex items-center justify-center">
              <Package className="w-5 h-5 text-info" />
            </div>
            <div>
              <h3 className="text-base font-semibold text-text-primary">Envíos Recientes</h3>
              <p className="text-text-muted text-xs">{filtrados.length} de {envios.length} registros</p>
            </div>
          </div>
          <div className="relative">
            <Search className="w-4 h-4 text-text-muted absolute left-3 top-1/2 -translate-y-1/2" />
            <input
              id="search-envios"
              type="text"
              placeholder="Buscar envío..."
              value={busqueda}
              onChange={(e) => setBusqueda(e.target.value)}
              className="w-full md:w-64 pl-9 pr-4 py-2 text-sm bg-surface-hover/50 border border-border rounded-xl text-text-primary placeholder:text-text-muted focus:outline-none focus:border-brand-500 focus:ring-1 focus:ring-brand-500/30 transition-all"
            />
          </div>
        </div>
      </div>

      <div className="overflow-x-auto flex-1">
        <table className="w-full text-left">
          <thead>
            <tr className="border-b border-border bg-surface-alt/40">
              <th className="px-4 py-3 text-text-muted text-[11px] uppercase tracking-wider font-semibold">ID</th>
              <th className="px-4 py-3 text-text-muted text-[11px] uppercase tracking-wider font-semibold">Remitente</th>
              <th className="px-4 py-3 text-text-muted text-[11px] uppercase tracking-wider font-semibold">Destinatario</th>
              <th className="px-4 py-3 text-text-muted text-[11px] uppercase tracking-wider font-semibold hidden lg:table-cell">Tipo</th>
              <th className="px-4 py-3 text-text-muted text-[11px] uppercase tracking-wider font-semibold hidden md:table-cell">Fecha</th>
              <th className="px-4 py-3 w-10"></th>
            </tr>
          </thead>
          <tbody>
            {filtrados.length === 0 ? (
              <tr>
                <td colSpan={6} className="px-4 py-12 text-center text-text-muted">
                  <Package className="w-10 h-10 mx-auto mb-3 opacity-30" />
                  <p className="text-sm">No se encontraron envíos</p>
                  {busqueda && <p className="text-xs mt-1">Intenta con otra búsqueda</p>}
                </td>
              </tr>
            ) : (
              filtrados.slice(0, 50).map((envio) => (
                <EnvioRow
                  key={envio.id}
                  envio={envio}
                  isExpanded={expandedId === envio.id}
                  onToggle={() => setExpandedId(expandedId === envio.id ? null : envio.id)}
                />
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  )
}
