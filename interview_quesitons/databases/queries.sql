create table teachers
(
    id           serial primary key,
    teacher_name varchar(50)

);

create table students
(
    id           serial primary key,
    student_name varchar(50)

);

create table courses
(
    id          serial primary key,
    course_name varchar(50),
    teacher_id  int references teachers (id)
);

create table student_courses
(
    course_id  int references courses,
    student_id int references students
);


select student_name, count(course_id) as cnt
from students
         left join student_courses sc on students.id = sc.student_id
group by student_id, student_name;

select student_name, cnt
FROM (
         select id, count(course_id) as cnt
         from students
                  left join student_courses sc on students.id = sc.student_id
         group by id
     ) T
         join students on T.id = students.id
order by cnt;
