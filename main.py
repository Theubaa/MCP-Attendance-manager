"""
Full Leave Management MCP Server
Author: You 😊

Usage:
    uv run main.py
"""

from datetime import date
from mcp.server.fastmcp import FastMCP

# Create MCP server instance
mcp = FastMCP("LeaveManagement")

# Employee leave balances
leave_balances = {
    "Gaurav": 15,
    "Shubha": 12,
    "Vibhanshu": 10,
    "Rajeev": 8,
    "Lakshay": 20
}

leave_policies = """
Company Leave Policy:
1. Annual leave: 20 days per year.
2. Sick leave: 10 days per year.
3. All leave requests must be approved by the manager.
4. Leave cancellation allowed up to 1 day before start date.
"""

# Store applied leaves: dict of {employee: list of requests}
leave_requests = {name: [] for name in leave_balances}


# ---- TOOLS ----

@mcp.tool()
def apply_leave(name: str, start_date: str, end_date: str, leave_type: str = "Annual") -> str:
    """Apply for leave with start and end dates."""
    if name not in leave_balances:
        return f"Error: No record found for {name}."

    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)
    days_requested = (end - start).days + 1

    if leave_balances[name] < days_requested:
        return f"Error: Not enough leave balance. Available: {leave_balances[name]} days."

    leave_balances[name] -= days_requested
    leave_requests[name].append({
        "start_date": start_date,
        "end_date": end_date,
        "leave_type": leave_type,
        "days": days_requested,
        "status": "Pending"
    })
    return f"✅ Leave applied for {name} ({leave_type}) from {start_date} to {end_date}. Remaining balance: {leave_balances[name]} days."


@mcp.tool()
def check_leave_balance(name: str) -> str:
    """Check available leave balance."""
    if name not in leave_balances:
        return f"No record found for {name}."
    return f"📅 {name} has {leave_balances[name]} days of leave remaining."


@mcp.tool()
def view_leave_requests(name: str) -> str:
    """View all leave requests for an employee."""
    if name not in leave_requests:
        return f"No record found for {name}."
    if not leave_requests[name]:
        return f"{name} has no leave requests."
    
    result = f"📋 Leave requests for {name}:\n"
    for i, req in enumerate(leave_requests[name], start=1):
        result += f"{i}. {req['leave_type']} leave from {req['start_date']} to {req['end_date']} ({req['days']} days) - Status: {req['status']}\n"
    return result.strip()


@mcp.tool()
def cancel_leave(name: str, request_number: int) -> str:
    """Cancel a leave request."""
    if name not in leave_requests or request_number <= 0 or request_number > len(leave_requests[name]):
        return f"Error: Invalid leave request number."

    req = leave_requests[name][request_number - 1]
    if req["status"] == "Cancelled":
        return "This leave request is already cancelled."

    # Refund leave days
    leave_balances[name] += req["days"]
    req["status"] = "Cancelled"
    return f"❌ Leave request #{request_number} for {name} has been cancelled. Balance restored to {leave_balances[name]} days."


# ---- RESOURCES ----

@mcp.resource("leave-policy://company")
def get_leave_policy() -> str:
    """Get the company's leave policy."""
    return leave_policies


# ---- PROMPTS ----

@mcp.prompt()
def leave_approval_message(name: str, approved: bool, reason: str = "") -> str:
    """Generate a leave approval or rejection message."""
    if approved:
        return f"Dear {name},\n\n✅ Your leave request has been approved.\nEnjoy your time off!"
    else:
        return f"Dear {name},\n\n❌ Unfortunately, your leave request has been rejected.\nReason: {reason}"


if __name__ == "__main__":
    mcp.run()
