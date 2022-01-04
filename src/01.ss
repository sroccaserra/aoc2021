(import (only (common) readlines))

(define huge 1000000000)

(define (solve-1 numbers)
  (let loop ([ns numbers])
    (let ([rest (cdr ns)])
      (if (null? rest) 0
          (if (< (car ns) (cadr ns))
              (+ 1 (loop rest))
              (loop rest))))))

(define (solve-2 numbers)
  (let loop ([ns numbers])
    (let ([rest (cdr ns)])
      (if (= 2 (length rest)) 0
          (let ([n1 (car ns)] [n2 (cadr ns)] [n3 (caddr ns)] [n4 (cadddr ns)])
            (if (< (+ n1 n2 n3) (+ n2 n3 n4))
                (+ 1 (loop rest))
                (loop rest)))))))

(let ([numbers (map string->number (readlines (cadr (command-line))))])
  (printf "~d\n" (solve-1 numbers))
  (printf "~d\n" (solve-2 numbers)))
