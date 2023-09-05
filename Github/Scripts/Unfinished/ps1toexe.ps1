# Install PS2EXE module
Install-Module -Name PS2EXE

# Prompt user for path to .ps1 file
$ps1FilePath = Read-Host "Enter the path to the .ps1 file you want to convert"

# Set path for output .exe file
$exeFilePath = "$($ps1FilePath.Replace('.ps1', '.exe'))"

# Convert .ps1 file to .exe file
Invoke-PS2EXE -Script $ps1FilePath -OutputFile $exeFilePath