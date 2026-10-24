import { defineConfig } from 'vite';

export default defineConfig({
  base: '/Rabbit./',
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    sourcemap: true,
    target: 'es2022'
  },
  server: {
    port: 5173,
    open: false
  }
});
