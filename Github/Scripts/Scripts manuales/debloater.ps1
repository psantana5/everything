
# Get current CPU usage and RAM consumption
$beforeCpu = Get-Process | Measure-Object CPU -Sum | Select-Object -ExpandProperty Sum
$beforeRam = (Get-Process | Measure-Object WorkingSet -Sum | Select-Object -ExpandProperty Sum) / 1MB

# Remove pre-installed apps
Get-AppxPackage *3DBuilder* | Remove-AppxPackage
# ... (rest of the app removal code)

# Disable unnecessary features
Disable-WindowsOptionalFeature -Online -FeatureName "Internet Explorer 11"
# ... (rest of the feature disabling code)

# Disable Cortana
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Search" -Name "BingSearchEnabled" -Value 0
# ... (rest of the Cortana disabling code)

Get-AppxPackage *3DBuilder* | Remove-AppxPackage
Get-AppxPackage *Alarms* | Remove-AppxPackage
Get-AppxPackage *BingFinance* | Remove-AppxPackage
Get-AppxPackage *BingNews* | Remove-AppxPackage
Get-AppxPackage *BingSports* | Remove-AppxPackage
Get-AppxPackage *BingWeather* | Remove-AppxPackage
Get-AppxPackage *GetHelp* | Remove-AppxPackage
Get-AppxPackage *GetStarted* | Remove-AppxPackage
Get-AppxPackage *Messaging* | Remove-AppxPackage
Get-AppxPackage *MicrosoftOfficeHub* | Remove-AppxPackage
Get-AppxPackage *MixedRealityPortal* | Remove-AppxPackage
Get-AppxPackage *MobilePlans* | Remove-AppxPackage
Get-AppxPackage *OfficeOneNote* | Remove-AppxPackage
Get-AppxPackage *OneConnect* | Remove-AppxPackage
Get-AppxPackage *OneDrive* | Remove-AppxPackage
Get-AppxPackage *People* | Remove-AppxPackage
Get-AppxPackage *Print3D* | Remove-AppxPackage
Get-AppxPackage *SkypeApp* | Remove-AppxPackage
Get-AppxPackage *SolitaireCollection* | Remove-AppxPackage
Get-AppxPackage *StickyNotes* | Remove-AppxPackage
Get-AppxPackage *Tips* | Remove-AppxPackage
Get-AppxPackage *Wallet* | Remove-AppxPackage
Get-AppxPackage *Whiteboard* | Remove-AppxPackage
Get-AppxPackage *WindowsMaps* | Remove-AppxPackage
Get-AppxPackage *XboxApp* | Remove-AppxPackage
Get-AppxPackage *XboxGameOverlay* | Remove-AppxPackage
Get-AppxPackage *XboxGamingOverlay* | Remove-AppxPackage
Get-AppxPackage *XboxIdentityProvider* | Remove-AppxPackage
Get-AppxPackage *XboxSpeechToTextOverlay* | Remove-AppxPackage

# Disable unnecessary features
Disable-WindowsOptionalFeature -Online -FeatureName "Internet Explorer 11"
Disable-WindowsOptionalFeature -Online -FeatureName "Windows Media Player"
Disable-WindowsOptionalFeature -Online -FeatureName "WindowsMediaPlayer"
Disable-WindowsOptionalFeature -Online -FeatureName "WorkFolders-Client"
Disable-WindowsOptionalFeature -Online -FeatureName "Xps-Foundation-Xps-Viewer"

# Disable Cortana
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Search" -Name "BingSearchEnabled" -Value 0
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Search" -Name "CortanaConsent" -Value 0
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Search" -Name "AllowCortana" -Value 0
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Search" -Name "SearchboxTaskbarMode" -Value 0

# Get CPU usage and RAM consumption after running the script
$afterCpu = Get-Process | Measure-Object CPU -Sum | Select-Object -ExpandProperty Sum
$afterRam = (Get-Process | Measure-Object WorkingSet -Sum | Select-Object -ExpandProperty Sum) / 1MB

# Calculate the difference in CPU usage and RAM consumption
$cpuDiff = $afterCpu - $beforeCpu
$ramDiff = $afterRam - $beforeRam

# Display the results
Write-Host "Before running the script, CPU usage was $beforeCpu. After running the script, CPU usage was $afterCpu. The difference is $cpuDiff."
Write-Host "Before running the script, RAM consumption was $beforeRam MB. After running the script, RAM consumption was $afterRam MB. The difference is $ramDiff MB."
# Get current CPU usage and RAM consumption
$beforeCpu = Get-Process | Measure-Object CPU -Sum | Select-Object -ExpandProperty Sum
$beforeRam = (Get-Process | Measure-Object WorkingSet -Sum | Select-Object -ExpandProperty Sum) / 1MB

#Si ves esto, sí, cómo suelo subir mis scripts a GitHub, 
#los hago en inglés para que la gente los pueda modificar/entender a su parecer 
#sin necesitar que me escriban para tonterías.