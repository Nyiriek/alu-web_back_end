import CLassroom from './0-classroom';

export default function initializeRooms() {
  const classRoomA = new CLassroom(19);
  const classRoomB = new CLassroom(20);
  const classRoomC = new CLassroom(34);

  return [classRoomA, classRoomB, classRoomC];
}
