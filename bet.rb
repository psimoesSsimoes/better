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

def write_in_mongo(doc)
        collection = $client[:bets]
        result = collection.insert_one(doc)
        puts result.n
end



#/div/div/div/div/div/input

def click(i)
	$b.li(:onclick => i.to_s).when_present.click
end


def Bet(doc,b)	
=begin
        b.td(:id, 'stakebox_2').set '1'
	puts doc.search('div/input').xpath('@id')
	sleep(10)
	doc = Nokogiri::HTML.parse(b.html)
	puts doc.search('td').xpath('text()')
=end
#/html/body/div[5]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/ul/li[1]/div[1]/div[2]
end



def retrive_wanted_odds(h)


	h.each {
		|i|
		 
		if $doBet==false
		unless i.to_s.split(',')[4].to_f > 1.30 #if it's the odd we are interested in
			if i.to_s.split(',')[4].to_s.include? '.' # if doesn't have the comma we don't want it
			    	$i*= i.to_s.split(',')[4].to_f #total of cotas
				#$oddsWanted << i
				puts i
				click(i)
				puts $i
				puts $doBet
				if $i>$Limit
					puts 'true'
					$doBet=true
					break	
				end

			end
		end
		
	end
	}
	return $oddsWanted

end

def read_page(h)
	unless $doBet == true		
	$b.li(:id => "#{h}").fire_event :onclick
	sleep(10)

 	$doc = Nokogiri::HTML.parse($b.html)
#	puts "###############################################################"
#	puts "############# Basquetebol ###################"
#	puts "###############################################################"
	$h1 = $doc.search('li').xpath('@onclick')
	puts retrive_wanted_odds($h1)
	end
end

########################################################

	$b = Watir::Browser.new
	$b.goto 'https://www.bet.pt/todays-events/'
	#/html/body/div[5]/div[3]/div[2]/div[1]/div[2]/div/ul/li[1]/ul/li	
 	$doc = Nokogiri::HTML.parse($b.html)
	
	$h2 = $doc.search('li/ul/li').xpath('@id')
        #puts $h2
        $h2.each { |x| 
			if(x.to_s.include? "tp") 
				read_page(x.to_s)
			end 
	}
#	if($doBet)	
		Bet($doc,$b)
#	end
