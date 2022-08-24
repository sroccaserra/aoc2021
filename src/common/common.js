import { readFileSync } from 'fs'

export function getInputLines() {
  const file = readFileSync(process.argv[2], 'utf8')
  return file.split('\n').slice(0, -1)
}

export class Queue {
  constructor() {
    this.values = []
  }
  enqueue(v) {
    this.values.push(v)
  }

  dequeue() {
    const result = this.values[0]
    this.values = this.values.slice(1)
    return result
  }

  size() {
     return this.values.length
  }
}
