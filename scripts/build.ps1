param()
$nodeDir = "C:\Users\Manik\AppData\Local\OpenAI\Codex\runtimes\cua_node\2b841c3d44b123ec\bin"
$env:Path = "$nodeDir;" + $env:Path
Write-Host "Node version: $(node -v)"
Set-Location "C:\Users\Manik\.gemini\antigravity\scratch\rabbit-app"
& "$nodeDir\corepack.cmd" pnpm run build
