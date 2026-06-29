import { Server, Cpu, CheckCircle } from 'lucide-react'

export default function InfraStatus() {
  return (
    <div className="bg-slate-900 rounded-xl p-5 border border-slate-800 shadow-sm h-full">
      <h3 className="text-lg font-semibold mb-4 text-slate-200">Infrastructure</h3>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="flex items-center justify-between p-4 bg-slate-800/50 rounded-lg">
          <div className="flex items-center gap-3">
            <Cpu className="w-6 h-6 text-emerald-400" />
            <div>
              <div className="text-sm text-slate-300">CPU Usage</div>
              <div className="text-xl font-bold text-white">34%</div>
            </div>
          </div>
          <div className="h-2 w-24 bg-slate-700 rounded-full overflow-hidden">
            <div className="h-full bg-emerald-400 w-[34%] rounded-full" />
          </div>
        </div>
        <div className="flex items-center justify-between p-4 bg-slate-800/50 rounded-lg">
          <div className="flex items-center gap-3">
            <Server className="w-6 h-6 text-sky-400" />
            <div>
              <div className="text-sm text-slate-300">Services</div>
              <div className="text-xl font-bold text-white">All Up</div>
            </div>
          </div>
          <CheckCircle className="w-6 h-6 text-emerald-400" />
        </div>
      </div>
    </div>
  )
}
