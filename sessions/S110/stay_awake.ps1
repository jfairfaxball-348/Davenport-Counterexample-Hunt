# Runtime-only idle-sleep inhibitor for the S110 campaign run (no settings changed).
# Holds ES_CONTINUOUS | ES_SYSTEM_REQUIRED while any support5_ shard process is alive, then exits.
Add-Type -Namespace Win32 -Name Power -MemberDefinition '[DllImport("kernel32.dll")] public static extern uint SetThreadExecutionState(uint esFlags);'
$ES_CONTINUOUS = [uint32]"0x80000000"; $ES_SYSTEM_REQUIRED = [uint32]"0x00000001"
[Win32.Power]::SetThreadExecutionState($ES_CONTINUOUS -bor $ES_SYSTEM_REQUIRED) | Out-Null
do {
  Start-Sleep -Seconds 60
  $alive = @(Get-CimInstance Win32_Process -Filter "Name='python.exe'" | Where-Object { $_.CommandLine -like '*support5_*' }).Count
} while ($alive -gt 0)
[Win32.Power]::SetThreadExecutionState($ES_CONTINUOUS) | Out-Null
