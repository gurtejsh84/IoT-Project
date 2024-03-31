package com.creativeteam.tn.attendancetrackingapplication

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.support.v7.widget.LinearLayoutManager
import android.util.Log
import android.view.View
import com.creativeteam.tn.attendancetrackingapplication.Adapter.EmployeeAttendanceAdapter
import com.creativeteam.tn.attendancetrackingapplication.Model.EmployeeAttendance
import com.parse.ParseObject
import com.parse.ParseQuery
import kotlinx.android.synthetic.main.activity_employee_attendance_list.*
import java.text.SimpleDateFormat
import java.util.*
import kotlin.collections.ArrayList

class EmployeeAttendanceListActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_employee_attendance_list)
        setTitle("Current Attendance")

        progressBar.visibility = View.VISIBLE

        val date = Calendar.getInstance().time
        val strDateFormat = "MM-dd-yyyy"
        val dateFormat = SimpleDateFormat(strDateFormat)
        val formattedDate = dateFormat.format(date)

        var list = ArrayList<EmployeeAttendance>()
        var adp = EmployeeAttendanceAdapter(this, list)
        rv_employee_attendance.layoutManager = LinearLayoutManager(this)
        rv_employee_attendance.adapter = adp

        val query = ParseQuery<ParseObject>("AttendanceTimes")
        query.whereEqualTo("date", formattedDate)
        query.include("employee")
        query.findInBackground{ attendanceList, e ->
            progressBar.visibility = View.GONE
            tvInfo.visibility = View.GONE
            if(e == null){
                if(attendanceList.size == 0){
                    tvInfo.visibility = View.VISIBLE
                }

                for (att in attendanceList){
                    var picture = att.getParseObject("employee")!!.getParseFile("picture")
                    var pictureURL= ""
                    if(picture!=null){
                        pictureURL = picture.url
                    }

                    var leavingTime =""
                    if(att.getString("leavingTime")!=null){
                        leavingTime = att.get("leavingTime").toString()
                    }

                    list.add(EmployeeAttendance(
                            att.objectId,
                            pictureURL,
                            att.getParseObject("employee")!!.get("name").toString(),
                            att.getParseObject("employee")!!.get("rfid").toString(),
                            att.getParseObject("employee")!!.get("ssn").toString(),
                            att.get("entryTime").toString(),
                            leavingTime
                    ))

                }
                adp.notifyDataSetChanged()
            }else{
                Log.d("EmployeeAttActivity", "Error: "+e.message)
            }
        }

    }
}
