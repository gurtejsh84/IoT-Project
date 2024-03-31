package com.creativeteam.tn.attendancetrackingapplication.Adapter

import android.content.Context
import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.creativeteam.tn.attendancetrackingapplication.Model.EmployeeAttendance
import com.creativeteam.tn.attendancetrackingapplication.R
import com.squareup.picasso.Picasso
import kotlinx.android.synthetic.main.employee_attendance_row.view.*

class EmployeeAttendanceAdapter(var c: Context, var list: ArrayList<EmployeeAttendance>) : RecyclerView.Adapter<RecyclerView.ViewHolder> () {
    override fun onCreateViewHolder(p0: ViewGroup, p1: Int): RecyclerView.ViewHolder {
        var my_view= LayoutInflater.from(p0.context).inflate(R.layout.employee_attendance_row, p0,false)
        return EmployeeAttendanceHolder(my_view)
    }

    override fun getItemCount(): Int {
        return list.size
    }

    override fun onBindViewHolder(p0: RecyclerView.ViewHolder, p1: Int) {

        (p0 as EmployeeAttendanceHolder).bind(list[p1])

    }

    class EmployeeAttendanceHolder(view: View) : RecyclerView.ViewHolder(view) {
        var pict_employee = view.picture_employee
        var employee_name = view.tv_employee_name
        var employee_ssn = view.tv_employee_ssn
        var employee_entry_time = view.tv_employee_entry_time
        var employee_leaving_time = view.tv_employee_leaving_time

        fun bind(empAttendance : EmployeeAttendance){
            employee_name.text = "Name: "+empAttendance.name
            employee_ssn.text = "SSN: "+empAttendance.ssn
            employee_entry_time.text = "Entry Time: "+empAttendance.entryTime
            employee_leaving_time.text = "Leaving Time: "+empAttendance.leavingTime

            if(empAttendance.pictureURL.length > 0){
                Picasso.get().load(empAttendance.pictureURL).into(pict_employee)
            }else{
                pict_employee.setImageResource(R.drawable.avatar)
            }

        }

    }
}