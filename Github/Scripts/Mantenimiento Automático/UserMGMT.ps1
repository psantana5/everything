# Import the NTFSSecurity module

Import-Module -Name NTFSSecurity

# Define the menu options
$menuOptions = @{
    "1" = "Create new local user"
    "2" = "Add user to local group"
    "3" = "Remove local user"
    "4" = "Remove user from local group"
}

# Display the menu and get the user's choice
do {
    Write-Host "`nMenu Options:`n"

    foreach ($option in $menuOptions.GetEnumerator() | Sort-Object Name) {
        Write-Host "$($option.Key): $($option.Value)"
    }

    $choice = Read-Host "`nEnter your choice (1-4, or Q to quit): "
} until ($choice -match '^[1234q]$' -and $choice -ne '')

# Perform the selected action based on the user's choice
switch ($choice) {
    1 {
        # Create a new local user account
        $username = Read-Host "Enter username for new account: "
        $password = Read-Host "Enter password for new account: "
        New-LocalUser -Name $username -Password (ConvertTo-SecureString $password -AsPlainText -Force)
        break
    }
    2 {
        # Add a user to a local group
        $username = Read-Host "Enter username to add to group: "
        $groupname = Read-Host "Enter name of group to add user to: "
        Add-LocalGroupMember -Group $groupname -Member $username
        break
    }
    3 {
        # Remove a local user account
        $username = Read-Host "Enter username of account to remove: "
        Remove-LocalUser -Name $username
        break
    }
    4 {
        # Remove a user from a local group
        $username = Read-Host "Enter username to remove from group: "
        $groupname = Read-Host "Enter name of group to remove user from: "
        Remove-LocalGroupMember -Group $groupname -Member $username
        break
    }
}