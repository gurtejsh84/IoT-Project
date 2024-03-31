package com.creativeteam.tn.attendancetrackingapplication.Model

data class EmployeeAttendance (var objectId: String,
                               var pictureURL: String,
                               var name: String,
                               var rfid: String,
                               var ssn: String,
                               var entryTime: String,
                               var leavingTime: String) {
}