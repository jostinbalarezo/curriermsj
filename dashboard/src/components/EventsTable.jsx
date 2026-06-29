import { AlertCircle } from 'lucide-react'

export default function EventsTable({ data }) {
  return (
    <div className="bg-slate-900 rounded-xl border border-slate-800 shadow-sm overflow-hidden">
      <div className="px-6 py-4 border-b border-slate-800 flex items-center justify-between">
        <h3 className="text-lg font-semibold text-slate-200">Recent Events</h3>
        <span className="text-xs text-slate-400 bg-slate-800 px-2 py-1 rounded-full">Last 15 min</span>
      </div>
      <div className="overflow-x-auto">
        <table className="w-full text-sm text-left text-slate-300">
          <thead className="text-xs text-slate-400 uppercase bg-slate-800/40">
            <tr>
              <th className="px-6 py-3 font-medium">Timestamp</th>
              <th className="px-6 py-3 font-medium">App</th>
              <th className="px-6 py-3 font-medium">Service</th>
              <th className="px-6 py-3 font-medium">Action</th>
              <th className="px-6 py-3 font-medium">Context</th>
            </tr>
          </thead>
          <tbody>
            {data.map((evt, idx) => (
              <tr key={evt.id} className={`${idx % 2 === 0 ? 'bg-slate-900' : 'bg-slate-900/50'} border-b border-slate-800 hover:bg-slate-800/70 transition-colors`}>
                <td className="px-6 py-4 font-mono text-xs text-slate-400">{new Date(evt.timestamp).toLocaleTimeString()}</td>
                <td className="px-6 py-4">{evt.app}</td>
                <td className="px-6 py-4"><span className="bg-slate-800 text-slate-300 px-2 py-1 rounded text-xs font-medium border border-slate-700">{evt.service}</span></td>
                <td className="px-6 py-4">{evt.action}</td>
                <td className="px-6 py-4">
                  <div className="flex flex-col gap-1">
                    <span>Latency: {evt.context.latency_ms}ms</span>
                    <span className="text-xs text-slate-500 font-mono">{evt.context.request_id}</span>
                    {evt.context.provider && (
                      <span className="flex items-center gap-1 text-amber-400 text-xs font-medium">
                        <AlertCircle className="w-3 h-3" /> Provider: {evt.context.provider}
                      </span>
                    )}
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}
