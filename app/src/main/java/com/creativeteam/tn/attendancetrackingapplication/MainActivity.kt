package com.creativeteam.tn.attendancetrackingapplication

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        setTitle("Main Menu")

        btnAddNewEmployee.setOnClickListener {
            val intent = Intent(this, AddNewEmployeeActivity :: class.java)
            startActivity(intent)
        }

        btnShowCurrentAttendance.setOnClickListener {
            val intent = Intent(this, EmployeeAttendanceListActivity :: class.java)
            startActivity(intent)
        }

        btnShowAttendanceHistory.setOnClickListener {
            val intent = Intent(this, EmployeeAttendanceHistoryActivity :: class.java)
            startActivity(intent)
        }

        btnEditChannels.setOnClickListener {
            val intent = Intent(this, ChannelsPreferencesActivity :: class.java)
            startActivity(intent)
        }

    }
}
