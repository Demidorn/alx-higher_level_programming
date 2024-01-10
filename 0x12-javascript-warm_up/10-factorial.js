#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1;
  }
  if (n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

module.exports = { factorial };
if (require.main === module) {
  const arg = process.argv[2];
  const num = parseInt(arg);

  console.log(`${factorial(num)}`);
}
