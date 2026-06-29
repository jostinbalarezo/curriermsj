import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts'

export default function LatencyChart({ data }) {
  return (
    <div className="bg-slate-900 rounded-xl p-5 border border-slate-800 shadow-sm">
      <h3 className="text-lg font-semibold mb-4 text-slate-200">Latency over time</h3>
      <div className="h-64">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
            <XAxis dataKey="time" stroke="#64748b" tick={{ fontSize: 12 }} />
            <YAxis stroke="#64748b" tick={{ fontSize: 12 }} />
            <Tooltip contentStyle={{ backgroundColor: '#0f172a', border: '1px solid #1e293b', borderRadius: '8px', color: '#f1f5f9' }} />
            <Line type="monotone" dataKey="latency" stroke="#34d399" strokeWidth={2} dot={false} />
            <Line type="monotone" dataKey="p95" stroke="#f472b6" strokeWidth={2} dot={false} />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  )
}
