Imports System.Net
Imports System.Net.Sockets

Module HostInfo
    Sub Main()
        Dim hostName As String = Environment.MachineName
        Console.WriteLine("Hostname: " & hostName)

        Try
            Dim ipHostInfo As IPHostEntry = Dns.GetHostEntry(hostName)
            Dim localIp As String = ""

            For Each address As IPAddress In ipHostInfo.AddressList
                If address.AddressFamily = AddressFamily.InterNetwork Then
                    localIp = address.ToString()
                    Exit For
                End If
            Next

            If Not String.IsNullOrEmpty(localIp) Then
                Console.WriteLine("IP Address: " & localIp)
            Else
                Console.WriteLine("Could not find a valid IPv4 address.")
            End If

        Catch ex As Exception
            Console.WriteLine("An error occurred: " & ex.Message)
        End Try

        Console.ReadKey()
    End Sub
End Module
