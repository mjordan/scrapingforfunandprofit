<?php
/**
 * Script to get titles from a web pages defined in an input list.
 * This is free and unencumbered software released into the public domain.
 */

$input_file = 'urls.txt';
$url_list = file($input_file);

foreach ($url_list as $url) {
  $html = file_get_contents(trim($url)); 
  $doc = new DOMDocument();
  // HTML is often not valid. Disable warnings generated
  // by PHP's XML parsing library.
  libxml_use_internal_errors(TRUE);
  if (!empty($html)) {
    $doc->loadHTML($html);
    libxml_clear_errors();
    // Get all the <title> elements, regardless of
    // location in the document.
    $xpath = new DOMXPath($doc);
    $titles = $xpath->query('//title');
    if ($titles->length > 0){
      foreach($titles as $title){
          print $title->nodeValue . "\n";
      }
    }
  }
}
?>
