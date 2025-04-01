export default function guardrail(mathFunction) {
  const queue = [];
  try {
    const result = mathFunction(); // Execute the provided math function
    queue.push(result); // If successful, push the result to the queue
  } catch (error) {
    queue.push(error.message); // If error occurs, push the error message to the queue
  }
  queue.push('Guardrail was processed'); // Always push this message
  return queue;
}
