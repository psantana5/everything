#Massive user deletion using a CSV file.

$user = Import-Csv -Path C:\Users\%username%\Downloads\usuarios.csv
foreach ($i in $user)
{
    Remove-LocalUser $i.nombre
}