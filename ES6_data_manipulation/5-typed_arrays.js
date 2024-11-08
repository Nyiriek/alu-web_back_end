export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const view = new Int8Array(buffer);

  try {
    view.setInt8(position, value);
  } catch (error) {
    return Error('Position outside range');
  }
  return view;
}
