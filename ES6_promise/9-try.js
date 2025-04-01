export default function guardrail(mathFunction) {
  const queue = [];

  try {
    // Execute the math function and append its result to the queue
    const result = mathFunction();
    queue.push(result);
  } catch (error) {
    // If an error occurs, append the error message to the queue
    queue.push(`Error: ${error.message}`);
  } finally {
    // In every case, append the guardrail message to the queue
    queue.push('Guardrail was processed');
  }

  return queue;
}
