import { Users, Repeat } from 'lucide-react'

export default function BusinessMetrics() {
  return (
    <div className="bg-slate-900 rounded-xl p-5 border border-slate-800 shadow-sm h-full">
      <h3 className="text-lg font-semibold mb-4 text-slate-200">Business Metrics</h3>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="flex items-center gap-4 p-4 bg-slate-800/50 rounded-lg">
          <Users className="w-8 h-8 text-sky-400" />
          <div>
            <div className="text-slate-400 text-sm">Connected Users</div>
            <div className="text-2xl font-bold text-white">1,284</div>
          </div>
        </div>
        <div className="flex items-center gap-4 p-4 bg-slate-800/50 rounded-lg">
          <Repeat className="w-8 h-8 text-amber-400" />
          <div>
            <div className="text-slate-400 text-sm">Payment Retries</div>
            <div className="text-2xl font-bold text-white">12</div>
          </div>
        </div>
      </div>
    </div>
  )
}
