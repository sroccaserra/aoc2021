import { readFileSync } from 'fs'

const huge = 9999999999

function solve_01_1(numbers) {
  let previous = huge
  let result = 0
  for (const n of numbers) {
    if (n > previous) {
      result++
    }
    previous = n
  }
  return result
}

function solve_01_2(numbers) {
	let [p1, p2, p3] = [huge, huge, huge]
	let result = 0
	for (const n of numbers) {
		if (n+p1+p2 > p1+p2+p3) {
			result++
		}
		[p1, p2, p3] = [n, p1, p2]
	}
	return result
}

const file = readFileSync(process.argv[2], 'utf8')
const numbers = file.split('\n').slice(0, -1).map(line => Number(line))

console.log(solve_01_1(numbers))
console.log(solve_01_2(numbers))
