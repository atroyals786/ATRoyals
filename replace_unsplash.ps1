$pattern = "https://images\.unsplash\.com/[^\"')\s]+"
Get-ChildItem -Recurse -Include *.html,*.js,*.css | ForEach-Object {
    $text = Get-Content -Path $_.FullName -Raw
    $new = [regex]::Replace($text, $pattern, 'Pics/1.jpeg')
    if ($new -ne $text) {
        Set-Content -Path $_.FullName -Value $new
        Write-Output "Updated $($_.FullName)"
    }
}
Write-Output 'Done'
