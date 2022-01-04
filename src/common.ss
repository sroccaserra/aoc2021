(library (common)
  (export readlines)
  (import (rnrs base)
          (rnrs io ports)
          (rnrs io simple))

  (define (readlines filename)
    (call-with-input-file
      filename
      (lambda (p)
        (let loop ([line (get-line p)]
                   [result '()])
          (if (eof-object? line)
              (reverse result)
              (loop (get-line p) (cons line result))))))))
