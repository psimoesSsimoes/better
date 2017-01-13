require 'open-uri'
require 'nokogiri'
require 'mongo'
require 'watir-webdriver'
require 'mechanize'
require 'mongo'

$i=1
$Limit=2.0
$doBet=false
$oddsWanted = []





	$b = Watir::Browser.new
	$b.goto 'https://www.bet.pt/todays-events/'
	#/html/body/div[5]/div[3]/div[2]/div[1]/div[2]/div/ul/li[1]/ul/li	
 	$doc = Nokogiri::HTML.parse($b.html)
	
	$h2 = $doc.search('li/ul/li').xpath('@id')
        #puts $h2
