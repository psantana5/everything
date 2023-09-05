<?php
// This PHP file is used to initiate the PDF download

$pdfURL = "URL_of_generated_PDF"; // Replace with the actual URL

header('Content-Type: application/pdf');
header('Content-Disposition: attachment; filename="code_documentation.pdf"');
readfile($pdfURL);
?>
