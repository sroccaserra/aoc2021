as yet unclassified
downloadInputForDay: dayNumber
	"comment stating purpose of message"
	| year url cookie session|
	year := 2021.
	url := 'https://adventofcode.com/',year,'/day/',dayNumber,'/input'.
      session := OSProcess accessor environmentAt: 'AOC_SESSION'.
	cookie := 'session=',session.

	^ (WebClient
		httpDo: [:client | client
				httpGet: url
				do: [:request | request headerAt: 'Cookie' put: cookie]]) content