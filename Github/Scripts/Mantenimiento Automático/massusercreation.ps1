#Massive user creation using a CSV file.

$user = Import-Csv -Path C:\Users\%username%\Downloads\usuarios.csv
foreach ($i in $user)
{
    $password = ConvertTo-SecureString $i.contra -AsPlainText -Force
    New-LocalUser $i.nombre -Password $password -AccountNeverExpires -PasswordNeverExpires
    Add-LocalGroupMember -group users -Member $i.nombre
}