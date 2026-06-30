import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      components: path.resolve(__dirname, 'src/components'),
      contexts: path.resolve(__dirname, 'src/contexts'),
      layouts: path.resolve(__dirname, 'src/layouts'),
      theme: path.resolve(__dirname, 'src/theme'),
      lib: path.resolve(__dirname, 'src/lib'),
      views: path.resolve(__dirname, 'src/views'),
      assets: path.resolve(__dirname, 'src/assets'),
      data: path.resolve(__dirname, 'src/data'),
    },
  },
})
