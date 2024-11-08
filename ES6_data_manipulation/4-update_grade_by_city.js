export default function updateStudentGradeByCity(arrayOfObjects, city, newGrades) {
  if (Array.isArray(arrayOfObjects) && typeof city === 'string' && Array.isArray(newGrades)) {
    return arrayOfObjects
      .filter((student) => student.location === city)
      .map((student) => {
        const gradeObj = newGrades.find((grade) => grade.studentId === student.id);
        return { ...student, grade: gradeObj ? gradeObj.grade : 'N/A' };
      });
  }
  return [];
}
