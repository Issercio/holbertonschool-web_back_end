export default function taskBlock(trueOrFalse) {
  let task = false;
  let task2 = true;

  if (trueOrFalse) {
    let taskInBlock = true;
    let task2InBlock = false;

    task = taskInBlock;
    task2 = task2InBlock;
  }

  return [task, task2];
}