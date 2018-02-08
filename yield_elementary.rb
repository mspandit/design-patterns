def calculation_with_operation(a, b, operation)
  operation.call(a, b)
end

def calculation_with_block(a, b)
  yield(a, b)
end

if 11 == calculation(5, 6, lambda { |a, b| a + b })
  STDOUT.write(".")
else
  STDOUT.write("*")
end
if 12 == calculation_with_block(6, 6) { |a, b| a + b }
  STDOUT.write(".")
else
  STDOUT.write("*")
end
