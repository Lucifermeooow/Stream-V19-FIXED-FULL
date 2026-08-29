import 'package:flutter_test/flutter_test.dart';
import 'package:stream_v19/main.dart';

void main() {
  testWidgets('Stream V19 renders', (WidgetTester tester) async {
    await tester.pumpWidget(const MyApp());

    expect(find.byType(MyApp), findsOneWidget);
  });
}
